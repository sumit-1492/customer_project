from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfiguration:

    root_dir: Path
    dataset_download_url: str
    zip_data_dir: Path
    unzip_data_dir: Path