# AWS::IAM::Role Policy JSON Verification Script

The script checks if JSON files, especially those following the AWS IAM policy format, have a specific condition:
whether the "Resource" field contains a single asterisk.

## Requirements
- Python 3.x
- JSON input file (example: `input.json`)

## Usage

### 1. Clone the repository:
```
git clone https://github.com/KRojowsky/aws-json-verifier.git
```
### 2. Navigate to the Directory: 
```
cd aws-json-verifier
```
### 3. Run the verification script:
Windows: 
```
python aws-json-verifier.py <json_file_path>
```
Linux: 
```
python3 aws-json-verifier.py <json_file_path>
```
### 3. Test cases:
Windows: 
```
python unit-tests.py <json_file_path>
```
Linux: 
```
python3 unit-tests.py <json_file_path>
```
