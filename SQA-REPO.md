Team Name: Palmer  
Team Members: Adrian Palmer (abp0058@auburn.edu)  
Comp 6710 Project  
Date: December 1, 2025


I selected 5 methods from the MLForensics codebase for property-based fuzzing using Hypothesis:I selected 5 methods from the MLForensics codebase for property-based fuzzing using Hypothesis:
 1. deleteRepo(dirName, type_) - mining/mining.py
     - I tested various directory names, including special characters and  empty strings
     
 2. makeChunks(the_list, size_) - mining/mining.py
   - I tested edge cases like empty lists, size=0, negative sizes, and large sizes

 3. dumpContentIntoFile(strP, fileP) - mining/mining.py
   - I tested various content lengths, special characters, and different filenames

 4. getAllSLOC(df_param, csv_encoding) - empirical/frequency.py
   - I tested empty dataFrames, missing files, and various encodings (utf-8, latin-1, ascii)

 5. String validation test
   - I tested String length validation and type checking

Fuzzing Results

Total Test Cases Run: ~100 (20 examples per method × 5 methods)

Bugs/Issues Found:
- No crashes detected during fuzzing
- `deleteRepo()` handles non-existent directories
- `makeChunks()` works correctly with various list sizes
- All methods handle edge cases appropriately


