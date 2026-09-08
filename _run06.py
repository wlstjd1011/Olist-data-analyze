"""노트북을 처음부터 끝까지 실행하고 출력을 파일에 저장한다.

    python _run06.py notebooks/06_delivery_expectation.ipynb

인자를 주지 않으면 06 을 실행한다. DuckDB 파일은 한 프로세스만 열 수 있으므로
VS Code 커널이 떠 있으면 먼저 종료해야 한다.
"""
import io
import sys

import nbformat
from nbclient import NotebookClient

path = sys.argv[1] if len(sys.argv) > 1 else 'notebooks/06_delivery_expectation.ipynb'
workdir = path.rsplit('/', 1)[0] + '/' if '/' in path else './'

nb = nbformat.read(io.open(path, encoding='utf-8'), as_version=4)
NotebookClient(nb, timeout=1200, kernel_name='python3',
               resources={'metadata': {'path': workdir}}).execute()
nbformat.write(nb, io.open(path, 'w', encoding='utf-8'))

errors = 0
for cell in nb.cells:
    for out in cell.get('outputs', []):
        if out.get('output_type') == 'error':
            errors += 1
            print('ERROR in', cell.get('id'))
            print('\n'.join(out.get('traceback', []))[-1200:])

print(f'{path} — cells: {len(nb.cells)}, errors: {errors}')
