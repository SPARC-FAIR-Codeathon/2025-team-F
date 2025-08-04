FROM python:3.10 as base
#
#  USAGE:
#     cd services/sparcats
#     docker build -f Dockerfile -t sparcats:prod --target production ../../
#     docker run sparcats:prod
#

LABEL maintainer=OmkarAthavale

# simcore-user uid=8004(${SC_USER_NAME}) gid=8004(${SC_USER_NAME}) groups=8004(${SC_USER_NAME})
ENV SC_USER_ID 8004
ENV SC_USER_NAME scu
RUN adduser --uid ${SC_USER_ID} --disabled-password --gecos "" --shell /bin/sh --home /home/${SC_USER_NAME} ${SC_USER_NAME}

RUN apt-get update \
    && apt-get -y install --no-install-recommends \
    jq \
    && rm --recursive --force /var/lib/apt/lists/*

# -------------------------- Build stage -------------------
# Installs build/package management tools and third party dependencies
#
# + /build             WORKDIR
#

#
FROM base as production

ENV SC_BUILD_TARGET production
ENV SC_BOOT_MODE production


ENV INPUT_FOLDER="/input" \
    OUTPUT_FOLDER="/output"


WORKDIR /home/${SC_USER_NAME}

# ------------------------------------------------------------------------------------
#TODO:
# uncomment and adapt to install runtime dependencies
#RUN apt-get update \
# && apt-get -y install --no-install-recommends \
# && rm -rf /var/lib/apt/lists/*
RUN pip install scipy tsaug pandas
# ------------------------------------------------------------------------------------

# copy source code
COPY --chown=${SC_USER_NAME}:${SC_USER_NAME} src/sparcats src/sparcats
# copy docker bootup scripts
COPY --chown=${SC_USER_NAME}:${SC_USER_NAME} docker/python/*.sh docker/
# copy simcore service cli
COPY --chown=${SC_USER_NAME}:${SC_USER_NAME} service.cli/ service.cli/
# necessary to be able to call run directly without sh in front
ENV PATH="/home/${SC_USER_NAME}/service.cli:${PATH}"

# ------------------------------------------------------------------------------------
#TODO:
# uncomment and provide a healtchecker if possible
# HEALTHCHECK --interval=30s \
#             --timeout=120s \
#             --start-period=30s \
#             --retries=3 \
#             CMD ["healthchecker app"]
# ------------------------------------------------------------------------------------

ENTRYPOINT [ "/bin/sh", "docker/entrypoint.sh" ]
CMD ["run"]
