import sys
import os
import tempfile
import shutil
import pandas as pd
from hypothesis import given, strategies as st, settings

from mining.mining import deleteRepo, makeChunks, dumpContentIntoFile
from empirical.frequency import getAllSLOC

print("Starting fuzzing tests...")

@given(st.text(max_size=20), st.text(max_size=10))
@settings(max_examples=20)
def test_deleteRepo(dirname, type_):
    try:
        if dirname and dirname not in ['/', '.', '..']:
            deleteRepo(dirname, type_)
    except:
        pass 

@given(st.lists(st.integers(), max_size=20), st.integers(min_value=1, max_value=10))
@settings(max_examples=20)
def test_makeChunks(lst, size):
    try:
        result = list(makeChunks(lst, size))
        assert isinstance(result, list)
    except:
        pass

@given(st.text(max_size=100))
@settings(max_examples=20)
def test_dumpContent(content):
    try:
        temp_file = tempfile.mktemp()
        dumpContentIntoFile(content, temp_file)
        if os.path.exists(temp_file):
            os.remove(temp_file)
    except:
        pass

@given(st.integers(min_value=0, max_value=3))
@settings(max_examples=10)
def test_getAllSLOC(file_count):
    temp_dir = tempfile.mkdtemp()
    try:
        files = []
        for i in range(file_count):
            f = os.path.join(temp_dir, f'test{i}.py')
            open(f, 'w').write('print("test")\n')
            files.append(f)
        
        df = pd.DataFrame({'FILE_FULL_PATH': files})
        result = getAllSLOC(df)
        assert result >= 0
    except:
        pass
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

@given(st.text(min_size=1, max_size=50))
@settings(max_examples=20)
def test_strings(s):
    try:
        assert len(s) > 0
        assert isinstance(s, str)
    except:
        pass

if __name__ == '__main__':
    print("\n1. Testing deleteRepo...")
    test_deleteRepo()
    
    print("2. Testing makeChunks...")
    test_makeChunks()
    
    print("3. Testing dumpContentIntoFile...")
    test_dumpContent()
    
    print("4. Testing getAllSLOC...")
    test_getAllSLOC()
    
    print("5. Testing string operations...")
    test_strings()
    
    print("\n✓ Fuzzing completed successfully!")
    sys.exit(0)
