from kfp.components._yaml_utils import load_yaml
from kfp.components._yaml_utils import dump_yaml
from kfp import components

SPEC = \
"""
name: dkube-training
description: |
    Component which can be used to do training for deep learning models on Dkube platform.
    Dkube training offers,
    * Advanced options for distributed training, gpu managment & pooling.
    * Support Hyper parameter tuning.
    * GDRDMA support for Horovod like training programs.
    * Ability to orchestrate and run custom training containers, prebuilt dkube datascience containers can also be used.
    * Renders nice Dashboard for training metrics and utilization graphs for GPU, CPU, Memory.
    * Support for early stopping if program is not converging - User can abort the Job and resume from previous point in training.
    * Tags to group related training jobs.
metadata:
  annotations: {platform: 'Dkube'}
  labels: {platform: 'Dkube', wfid: '{{workflow.uid}}', runid: '{{pod.name}}', stage: 'training'}
inputs:
  - {name: auth_token,      type: String,   optional: false,
     description: 'Required. Dkube authentication token.'}
  - {name: container,       type: Dict,     optional: false,
     description: 'Required. Container to use for training. Format: {"image":<url>, "username":<>, "password":<>}'}
  - {name: program,         type: String,   optional: true,     default: '',
     description: 'Optional. Program imported in Dkube to be run inside container. If not specified container should have entrypoint.'}
  - {name: run_script,      type: String,   optional: true,     default: '',
     description: 'Optional. Script to run the program. If not specified container should have entrypoint.'}
  - {name: datasets,        type: List,     optional: true,     default: '[]',
     description: 'Optional. List of input datasets required for training. These datasets must be created in Dkube.'}
  - {name: models,          type: List,     optional: true,     default: '[]',
     description: 'Optional. List of pretrained models required for training. These models must be created in Dkube.'}
  - {name: ngpus,           type: Integer,  optional: true,     default: 0,
     description: 'Optional. Number of gpus the training program should use.'}
  - {name: nworkers,        type: Integer,  optional: true,     default: 0,
     description: 'Optional. Number of workers for training, >0 for distributed training.'}
  - {name: auto_distribute, type: String,   optional: true,     default: 'false',
     description: 'Optional. Should Dkube auto distribute based on available number of resources.'}
  - {name: config,          type: String,   optional: true,      default: '',
    description: 'Optional. HP file or configuration data required for training program.
                  Supported inputs - 
                  d3s://<path> - Path to a file in dkube storage.
                  <string> - Inline data'}
  - {name: tuning,          type: String,   optional: true,     default: '',
     description: 'Optional. HP tuning information. Can be a URL to a file with hptuning definition or inline data.
                   Supported inputs -
                   d3s://<path> - Path to a file in dkube storage.
                   <string> - Inline data, only json formatted string is valid.'}
  - {name: envs,            type: List,     optional: true,     default: '[]',
     description: 'Optional. Environments for training program. Exact key value will be made available for the container'}
  - {name: gdrdma,          type: String,   optional: true,     default: 'false',
     description: 'Optional. Whether to use GDRDMA for distributed training.'}
  - {name: access_url,      type: String,   optional: true,     default: '',
     description: 'Optional. URL at which dkube is accessible, copy paste from the browser of this window. Required for cloud deployments.'}
outputs:
  - {name: rundetails,      description: 'Details of the dkube run'}
  - {name: artifact,        description: 'Identifier in Dkube storage where artifacts of training are stored.'}
implementation:
  container:
    image: ocdr/dkubepl:1.4.0
    command: ['dkubepl']
    args: [
      training,
      --accessurl, {inputValue: access_url},
      --token, {inputValue: auth_token},
      --container, {inputValue: container},
      --script, {inputValue: run_script},
      --program, {inputValue: program},
      --datasets, {inputValue: datasets},
      --models, {inputValue: models},
      --ngpus, {inputValue: ngpus},
      --nworkers, {inputValue: nworkers},
      --auto, {inputValue: auto_distribute},
      --config, {inputValue: config},
      --tuning, {inputValue: tuning},
      --envs, {inputValue: envs},
      --gdrdma, {inputValue: gdrdma},
      --runid, '{{pod.name}}'
    ]
    fileOutputs:
      rundetails:   /tmp/rundetails
      artifact:     /tmp/artifact
"""

def DkubeTrainOp(name='dkube-training'):
    cdict = load_yaml(SPEC)
    cdict['name'] = name
    cyaml = dump_yaml(cdict)

    return components.load_component_from_text(cyaml)