# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
# http:# www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.http import Http404

from kafka.conf import CLUSTERS
import socket



def get_cluster_or_404(id):
  """ Get a cluster information from its ID or a 404 Error """
  try:
    name = id
    cluster = CLUSTERS.get()[name]
  except (TypeError, ValueError, KeyError):
    raise Http404()

  cluster = {
    'id': id,
    'nice_name': id,
    'zk_host_ports': cluster.ZK_HOST_PORTS.get(),
    'brokers_path' : cluster.BROKERS_PATH.get(),
    'consumers_path' : cluster.CONSUMERS_PATH.get(),
    'topics_path' : cluster.TOPICS_PATH.get(),
    'ganglia_server' : cluster.GANGLIA_SERVER.get(),
    'ganglia_data_source' : cluster.GANGLIA_DATA_SOURCE.get(),
  }

  return cluster

def test_connection (host, port):
  """ Test available connection of a given host and port """
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    s.connect((host, port))
    return
  except socket.error:
    return "Error"
  s.close()