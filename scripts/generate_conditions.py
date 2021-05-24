#!/usr/bin/env python3

condition_strings = [
    "ArnEquals",
    "ArnNotEquals",
    "ArnLike",
    "ArnNotLike",
    "Bool",
    "DateEquals",
    "DateNotEquals",
    "DateLessThan",
    "DateLessThanEquals",
    "DateGreaterThan",
    "DateGreaterThanEquals",
    "IpAddress",
    "NotIpAddress",
    "Null",
    "NumericEquals",
    "NumericNotEquals",
    "NumericLessThan",
    "NumericLessThanEquals",
    "NumericGreaterThan",
    "NumericGreaterThanEquals",
    "StringEquals",
    "StringNotEquals",
    "StringEqualsIgnoreCase",
    "StringNotEqualsIgnoreCase",
    "StringLike",
    "StringNotLike",
]

condition_qualifier_strings = ["ForAnyValue", "ForAllValues"]


def make_condition(type_name: str, condition_name: str) -> None:
    print(f'class {type_name}(ConditionElement):')
    print(f'    condition = "{condition_name}"')
    print("")
    print("")
    print(f'class {type_name}IfExists(ConditionElement):')
    print(f'    condition = "{condition_name}IfExists"')
    print("")
    print("")

    # Previous dynamic creation in aws.py
    #
    # globals()[type_name] = type(
    #    type_name, (ConditionElement,), dict(condition=condition_name)
    # )
    # globals()[type_name + "IfExists"] = type(
    #    type_name + "IfExists",
    #    (ConditionElement,),
    #    dict(condition=condition_name + "IfExists"),
    # )


# Create condition classes
for condition in condition_strings:
    make_condition(condition, condition)

    for qual in condition_qualifier_strings:
        make_condition(f"{qual}{condition}", f"{qual}:{condition}")
