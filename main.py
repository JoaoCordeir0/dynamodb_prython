import boto3

# Inicializa o cliente do DynamoDB
dynamodb = boto3.client('dynamodb')

# Executa a operação list_tables() para listar as tabelas
def list_tables():    
    response = dynamodb.list_tables()

    print("Tabelas do DynamoDB:")
    for table in response['TableNames']:
        print(table)

# Executa a operação scan() para listar todos os itens da tabela
def list_table_values():        
    response = dynamodb.scan(TableName='Users')
    
    for item in response['Items']:        
        print(item)

list_tables()
list_table_values()