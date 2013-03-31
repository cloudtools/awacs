from awacs.aws import Action, Allow, Policy, Statement


pd = Policy(
    Statement=[
        Statement(
            Effect=Allow,
            Action=[Action("sdb", "*"), Action("s3", "*")],
            Resource=["arn:aws:s3:::my_corporate_bucket/*"],
        ),
    ],
)
print(pd.to_json())
