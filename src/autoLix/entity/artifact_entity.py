from dataclasses import dataclass

# Data Ingestion Artifacts
@dataclass
class DataIngestionArtifact:
    reddit_data_file_path: str
    wiki_data_file_path: str
    external_data_file_path: str

# Data Transformation Artifacts
@dataclass
class DataTransformationArtifacts:
    transformed_data_path: str