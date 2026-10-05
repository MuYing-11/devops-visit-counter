FROM jenkins/jenkins:lts-jdk17

USER root
# Python to run the unit tests, docker CLI to build/push the image
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-venv \
    && rm -rf /var/lib/apt/lists/* \
    && git config --system --add safe.directory '*'
COPY --from=docker:cli /usr/local/bin/docker /usr/local/bin/docker

USER jenkins
RUN jenkins-plugin-cli --plugins git workflow-aggregator junit credentials-binding \
    configuration-as-code job-dsl

# Configuration as code: admin user, Docker Hub credentials and the pipeline job
COPY casc.yaml /usr/share/jenkins/ref/casc.yaml
ENV CASC_JENKINS_CONFIG=/usr/share/jenkins/ref/casc.yaml
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false -Dhudson.plugins.git.GitSCM.ALLOW_LOCAL_CHECKOUT=true"
