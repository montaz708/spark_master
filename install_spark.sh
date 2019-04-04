#!/bin/bash

set -x

wget https://www-eu.apache.org/dist/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz
tar -xzf spark-2.4.0-bin-hadoop2.7.tgz -C /opt/
cp /local/repository/spark-env.sh /opt/spark-2.4.0-bin-hadoop2.7/conf/spark-env.sh