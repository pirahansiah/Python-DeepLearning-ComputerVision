# Python-DeepLearning-ComputerVision

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Deep Learning](https://img.shields.io/badge/Deep%20Learning-Computer%20Vision-red)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Python utilities for modifying and splitting Kaggle datasets for Deep Learning Computer Vision applications.

## Overview

This repository provides scripts to:
- **Copy files** from large dataset folders by count or label
- **Filter and split** CSV-based image datasets by class labels
- Prepare training/validation/test splits for CV model training

## Scripts

| Script | Description |
|--------|-------------|
| `Farshid-PirahanSiah-copy-files.py` | Copy a specified number of files from a source directory to a destination |
| `FarshidPirahanSiah_Python.py` | Read a CSV manifest and copy images matching a specific class label |

## Usage

### Copy Files by Count
```python
# Edit paths in Farshid-PirahanSiah-copy-files.py
source_dir = '/path/to/kaggle/dataset'
dest_dir = '/path/to/output'
max_files = 1000  # Number of files to copy

for files in os.listdir(source_dir)[:max_files]:
    copyfile(os.path.join(source_dir, files), os.path.join(dest_dir, files))
```

### Filter by CSV Label
```python
# Edit paths in FarshidPirahanSiah_Python.py
with open('labels.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if int(row[1]) == 1:  # Column index to filter
            copyfile(src + row[0], dst + row[0])
```

## 2025–2026: Modern Dataset Management

| Tool | Use Case |
|------|----------|
| **FiftyOne** | Visual dataset curation, model evaluation, quality analysis |
| **Roboflow** | Auto-labeling, dataset versioning, export to any format |
| **Albumentations** | Advanced augmentation pipelines (2025: GPU-accelerated transforms) |
| **TorchData / tf.data** | Streaming large-scale datasets without full download |
| **WebDataset** | Sharded, streaming-first dataset format for distributed training |
| **HuggingFace Datasets** | Parquet-backed, lazy-loading dataset hub |

### Recommended Workflow (2025+)

```
Kaggle Download → Roboflow/FiftyOne Curation → Albumentations Augmentation
     ↓                                              ↓
  Raw Images                            Clean, Balanced Splits
     ↓                                              ↓
  WebDataset Shards ←────────────── Train / Val / Test
```

### Key Libraries

```bash
pip install fiftyone roboflow albumentations webdataset
pip install torch torchvision ultralytics  # For model training
```

## Requirements

```
numpy
pandas
Pillow
opencv-python
```

## Related Projects

- [cv-ml-pipline](https://github.com/pirahansiah/cv-ml-pipline) — CV/ML pipeline tools
- [CD4ML-Scenarios](https://github.com/pirahansiah/CD4ML-Scenarios) — Continuous Delivery for ML

## Author

**Farshid Pirahansiah**
- Website: [pirahansiah.com](https://www.pirahansiah.com)
- GitHub: [github.com/pirahansiah](https://github.com/pirahansiah)
- LinkedIn: [linkedin.com/in/pirahansiah](https://www.linkedin.com/in/pirahansiah)

## License

MIT License — See [LICENSE](LICENSE) for details.
