# ROADMAP.md — Python-DeepLearning-ComputerVision

## 12-Month Vision (2026 Q3 – 2027 Q2)

Evolve from standalone utility scripts into a full-featured dataset management library with CLI tools, configuration-driven pipelines, and integration with modern CV training frameworks.

### Q3 2026 — Library Foundation
- Refactor scripts into a proper Python package with `pip install` support
- Add CLI interface (`cvdata split`, `cvdata filter`, `cvdata balance`)
- Implement YAML/JSON configuration for dataset operations
- Add type hints, docstrings, and unit tests (pytest)

### Q4 2026 — Smart Features
- Implement automatic class-balance detection and rebalancing
- Add dataset quality analysis (duplicate detection, corrupt image filtering)
- Integrate FiftyOne SDK for visual dataset exploration
- Support streaming datasets from cloud storage (S3, GCS, Azure Blob)

### Q1 2027 — Advanced Pipeline
- Add Albumentations-based augmentation pipeline with preview
- Implement WebDataset shard generation for distributed training
- Create Roboflow integration for auto-labeling and version control
- Support HuggingFace Datasets format for ecosystem compatibility

### Q2 2027 — Production Ready
- Add dataset versioning with metadata tracking
- Implement incremental dataset updates (add new classes without full rebuild)
- Create MLOps integration (MLflow, Weights & Biases experiment tracking)
- Add ONNX/TensorRT export pipeline for edge deployment

## Technical Debt

| Item | Priority | Description |
|------|----------|-------------|
| No package structure | High | Scripts not installable; no `setup.py`/`pyproject.toml` |
| Hardcoded paths | High | Scripts require manual path editing in source code |
| Python 2 syntax | High | `print strb[0]` syntax in FarshidPirahanSiah_Python.py |
| No tests | Medium | Zero unit tests or integration tests |
| No type hints | Medium | Missing modern Python typing |
| No error handling | Medium | Silent failures on missing files/directories |
| Dependency pinning | Low | Requirements not formally specified |

## Future Features

- **Dataset Profiler**: Automated analysis of dataset statistics, class distribution, image quality
- **Smart Splitter**: ML-powered train/val/test splitting that optimizes for model performance
- **Augmentation Recommender**: Suggest augmentation strategies based on dataset characteristics
- **Cloud Dataset Connector**: Direct integration with Kaggle API, Roboflow, CVAT
- **Dataset Diff Tool**: Compare two dataset versions and visualize changes
- **Multi-Modal Support**: Extend beyond images to video, audio, and text datasets
- **Collaborative Datasets**: Team-based dataset curation with conflict resolution
