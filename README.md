# orcapod-extension-spikeinterface

OrcaPod extension for [SpikeInterface](https://spikeinterface.readthedocs.io/) types.

Adds native support for `BaseRecording`, `BaseSorting`, `Motion`, and `SortingAnalyzer`
objects as first-class orcapod value types.

## Installation

```bash
pip install orcapod-extension-spikeinterface
```

## Usage

```python
import orcapod as op
from orcapod_extension_spikeinterface import spikeinterface_extension

# Register SI types into the default orcapod context at startup
op.register_extension(spikeinterface_extension)
```

After registration, SpikeInterface objects can be used as typed inputs/outputs in
orcapod `FunctionPod` functions.

## License

MIT
