FROM container-registry.oracle.com/os/oraclelinux:9-slim

COPY rpms /tmp/

RUN microdnf update -y && \
    microdnf clean all && \
    rpm -i /tmp/*.rpm && \
    rm -rf /var/cache/yum/* /var/lib/rpm/* /tmp/*.rpm && \
    chown -R 1001:1001 /var/dex && \
    chown -R 1001:1001 /etc/dex

USER 1001:1001

CMD ["dex", "serve", "/etc/dex/config.docker.yaml"]
