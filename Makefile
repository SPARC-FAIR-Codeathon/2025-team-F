#
# Author: Omkar Athavale

SHELL = /bin/sh
.DEFAULT_GOAL := help

export VCS_URL    := $(shell git config --get remote.origin.url 2> /dev/null || echo unversioned repo)
export VCS_REF    := $(shell git rev-parse --short HEAD 2> /dev/null || echo unversioned repo)
export VCS_STATUS := $(if $(shell git status -s 2> /dev/null || echo unversioned repo),'modified/untracked','clean')
export BUILD_DATE := $(shell date -u +"%Y-%m-%dT%H:%M:%SZ")

export DOCKER_IMAGE_NAME ?= sparcatsfix
export DOCKER_IMAGE_TAG ?= 0.1.1

OSPARC_DIR:=$(CURDIR)/.osparc

APP_NAME := sparcatsfix

# Builds new service version ----------------------------------------------------------------------------

define _bumpversion
	# upgrades as $(subst $(1),,$@) version, commits and tags
	@docker run -it --rm -v $(PWD):/${DOCKER_IMAGE_NAME} \
		-u $(shell id -u):$(shell id -g) \
		itisfoundation/ci-service-integration-library:v2.1.25\
		sh -c "cd /${DOCKER_IMAGE_NAME} && bump2version --verbose --list --config-file $(1) $(subst $(2),,$@)"
endef

.PHONY: version-patch version-minor version-major
version-patch version-minor version-major: .bumpversion.cfg ## increases service's version
	@make compose-spec
	@$(call _bumpversion,$<,version-)
	@make compose-spec

.PHONY: compose-spec
compose-spec: ## runs ooil to assemble the docker-compose.yml file
	@docker run --rm -v $(PWD):/${DOCKER_IMAGE_NAME} \
		-u $(shell id -u):$(shell id -g) \
		itisfoundation/ci-service-integration-library:v2.1.25\
		sh -c "cd /${DOCKER_IMAGE_NAME} && ooil compose"

build: | compose-spec	## build docker image
	docker compose build

# To test built service locally -------------------------------------------------------------------------
.PHONY: run-local
run-local:	## runs image with local configuration
	docker compose --file docker-compose-local.yml up

.PHONY: publish-local
publish-local: ## push to local throw away registry to test integration
	docker tag simcore/services/comp/${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} registry:5000/simcore/services/comp/$(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG)
	docker push registry:5000/simcore/services/comp/$(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG)
	@curl registry:5000/v2/_catalog | jq

.PHONY: help
help: ## this colorful help
	@echo "Recipes for '$(notdir $(CURDIR))':"
	@echo ""
	@awk 'BEGIN {FS = ":.*?## "} /^[[:alpha:][:space:]_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""


# COOKIECUTTER -----------------------------------------------------------------

.PHONY: replay
replay: .cookiecutterrc ## re-applies cookiecutter
	# Replaying gh:ITISFoundation/cookiecutter-osparc-service ...
	@cookiecutter --no-input --overwrite-if-exists \
		--config-file=$< \
		--output-dir="$(abspath $(CURDIR)/..)" \
		"gh:ITISFoundation/cookiecutter-osparc-service"


.PHONY: info
info: ## general info
	# env vars: version control
	@echo " VCS_URL                     : $(VCS_URL)"
	@echo " VCS_REF                     : $(VCS_REF)"
	@echo " VCS_STATUS                  : $(VCS_STATUS)"
	# env vars: docker
	@echo " DOCKER_IMAGE_TAG            : $(DOCKER_IMAGE_TAG)"
	@echo " BUILD_DATE                  : $(BUILD_DATE)"
	# exe: recommended dev tools
	@echo ' git                         : $(shell git --version 2>/dev/null || echo not found)'
	@echo ' make                        : $(shell make --version 2>&1 | head -n 1)'
	@echo ' jq                          : $(shell jq --version 2>/dev/null || echo not found z)'
	@echo ' awk                         : $(shell awk -W version 2>&1 | head -n 1 2>/dev/null || echo not found)'
	@echo ' python                      : $(shell python3 --version 2>/dev/null || echo not found )'
	@echo ' docker                      : $(shell docker --version)'
	@echo ' docker buildx               : $(shell docker buildx version)'
	@echo ' docker compose              : $(shell docker compose --version)'

# MISC -----------------------------------------------------------------


.PHONY: clean
git_clean_args = -dxf --exclude=.vscode/

clean: ## cleans all unversioned files in project and temp files create by this makefile
	# Cleaning unversioned
	@git clean -n $(git_clean_args)
	@echo -n "Are you sure? [y/N] " && read ans && [ $${ans:-N} = y ]
	@echo -n "$(shell whoami), are you REALLY sure? [y/N] " && read ans && [ $${ans:-N} = y ]
	@git clean $(git_clean_args)
