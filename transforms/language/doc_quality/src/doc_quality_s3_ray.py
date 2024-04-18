# (C) Copyright IBM Corp. 2024.
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

import os
import sys

from data_processing.ray import TransformLauncher
from data_processing.utils import ParamsUtils
from doc_quality_transform import DocQualityTransformConfiguration


print(os.environ)
# create launcher
launcher = TransformLauncher(transform_runtime_config=DocQualityTransformConfiguration())
# create parameters
s3_cred = {
    "access_key": "localminioaccesskey",
    "secret_key": "localminiosecretkey",
    "url": "http://localhost:9000",
}
s3_conf = {
    "input_folder": "test/doc_quality/input",
    "output_folder": "test/doc_quality/output",
}

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
docq_params = {
    "docq_text_lang": "en",
    "docq_doc_content_column": "contents",
    "docq_bad_word_filepath": basedir + "/ldnoobw/en",
    "docq_kenLM_model": basedir + "/lm_sp/",
}
worker_options = {"num_cpus": 0.8}
code_location = {"github": "github", "commit_hash": "12345", "path": "path"}
params = {
    "run_locally": True,
    "max_files": -1,
    "s3_cred": ParamsUtils.convert_to_ast(s3_cred),
    "s3_config": ParamsUtils.convert_to_ast(s3_conf),
    "worker_options": ParamsUtils.convert_to_ast(worker_options),
    "num_workers": 5,
    "checkpointing": False,
    "pipeline_id": "pipeline_id",
    "job_id": "job_id",
    "creation_delay": 0,
    "code_location": ParamsUtils.convert_to_ast(code_location),
}
sys.argv = ParamsUtils.dict_to_req(d=params | docq_params)

# launch
launcher.launch()