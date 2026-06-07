import subprocess
import sys

print("Step 1: Running data pipeline...")
subprocess.run([sys.executable, 'src/data_pipeline.py'], check=True)

print("Step 2: Running ranking engine...")
subprocess.run([sys.executable, 'src/ranking_engine.py'], check=True)

print("Step 3: Running visualization...")
subprocess.run([sys.executable, 'src/visualization.py'], check=True)

print("Done. Check data/processed/ for CSVs and graphs/ for plots.")