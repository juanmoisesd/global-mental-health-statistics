import os

def test_data_dirs_exist():
    assert os.path.exists("data/raw")
    assert os.path.exists("data/clean")
    assert os.path.exists("data/analysis_ready")

def test_license_exists():
    assert os.path.exists("LICENSE")
