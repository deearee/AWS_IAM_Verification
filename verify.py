import sys
import json
import os


# Sprawdza czy content jest stringiem JSONowym w formacie AWS::IAM::Role Policy
# Jesli tak to zwraca sparsowany JSON
# W przeciwnym razie rzuca wyjatek
def parse_and_check_format(content):
    parsed_json = json.loads(content) # Sprawdza czy content to string JSONowy
    
    # Sprawdza (powierzchownie) format AWS::IAM::Role Policy
    if "PolicyDocument" not in parsed_json or "PolicyName" not in parsed_json:
        raise ValueError("Content isn't in AWS::IAM::Role Policy format.")
    
    policy_document = parsed_json["PolicyDocument"]
    if "Statement" not in policy_document:
        raise ValueError("A AWS::IAM::Role Policy requires a statement.")

    return parsed_json


# Zwraca False jesli content jest w formacie AWS::IAM::Role Policy i zawiera Statement z polem "Resource": "*". W przeciwnym razie zwraca True
# Rzuca wyjatek jesli content nie jest stringiem JSONowym lub nie jest w w formacie AWS::IAM::Role Policy
def verify_json(content):
    def statement_has_asterisk_resource(statement):
        if "Resource" in statement and (statement["Resource"] == "*" or statement["Resource"] == ["*"]):
            return True
        return False
    
    policy_document = parse_and_check_format(content)["PolicyDocument"]

    if isinstance(policy_document["Statement"], list): # W przypadku listy Statement
        for statement in policy_document["Statement"]:
            if statement_has_asterisk_resource(statement):
                return False
    else: # W przypadku obiektu Statement
        if statement_has_asterisk_resource(policy_document["Statement"]):
            return False

    return True


# Podaj JSON na wejsciu standardowym lub podaj sciezke do pliku w pierwszym argumencie
if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if os.path.exists(file_path):
            print(verify_json(open(file_path).read()))
        else:
            print("The file doesn't exist.")
    else:
        json_input = sys.stdin.read()
        print(verify_json(json_input))