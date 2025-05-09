#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""
Example DAG using GCSToPrestoOperator.
"""

from __future__ import annotations

import os
from datetime import datetime

from airflow import models
from airflow.providers.presto.transfers.gcs_to_presto import GCSToPrestoOperator

BUCKET = os.environ.get("GCP_GCS_BUCKET", "test28397yeo")
PATH_TO_FILE = os.environ.get("GCP_PATH", "path/to/file")
PRESTO_TABLE = os.environ.get("PRESTO_TABLE", "test_table")
ENV_ID = os.environ.get("SYSTEM_TESTS_ENV_ID")
DAG_ID = "example_gcs_to_presto"

with models.DAG(
    dag_id=DAG_ID,
    schedule="@once",  # Override to match your needs
    start_date=datetime(2022, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:
    # [START gcs_csv_to_presto_table]
    gcs_csv_to_presto_table = GCSToPrestoOperator(
        task_id="gcs_csv_to_presto_table",
        source_bucket=BUCKET,
        source_object=PATH_TO_FILE,
        presto_table=PRESTO_TABLE,
    )
    # [END gcs_csv_to_presto_table]


from tests_common.test_utils.system_tests import get_test_run  # noqa: E402

# Needed to run the example DAG with pytest (see: tests/system/README.md#run_via_pytest)
test_run = get_test_run(dag)
