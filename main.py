import boto3

# Inicializa o cliente do DynamoDB
dynamodb = boto3.client('dynamodb')

# Executa a operação list_tables() para listar as tabelas
def list_tables():    
    response = dynamodb.list_tables()

    print('Tabelas do DynamoDB:')
    for table in response['TableNames']:
        print(table)

# Executa a operação scan() para listar todos os itens da tabela
def list_table_values():        
    response = dynamodb.scan(TableName='Users')
    
    print('Valores na tabela:')
    for item in response['Items']:        
        print(item)

# Executa a operação Query() para procurar itens com base em um índice ou chave primária
def list_table_value_by_value(value):    
    response = dynamodb.query(
        TableName='Users',
        KeyConditionExpression='user_id = :val',
        ExpressionAttributeValues={
            ':val': {'S': value}  # 'S' indica que o valor é uma string
        }
    )

    print(f'Valor da busca por "{value}":')
    for item in response['Items']:        
        print(item)

# Execute a operação put_item() para adicionar o novo registro à tabela
def create_item_in_table():
    data = {
        'user_id': {'S': 'gisele2'}, 
        'user_hash': {'S': 'gcj'},
        # 'complete_name': {'S': 'Gisele Cristina Joaquim'},
    }    
    
    response = dynamodb.put_item(
        TableName='Users',
        Item=data
    )
    
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print('Novo registro adicionado com sucesso!')
    else:
        print('Falha ao adicionar novo registro. Detalhes:', response)

# Execute a operação delete_item() para excluir o item da tabela
def delete_item_in_table(user_id, user_hash):        
    response = dynamodb.delete_item(
        TableName='Users',
        Key={
            'user_id': {'S': user_id},
            'user_hash': {'S': user_hash} 
        },                
    )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print('Item excluído com sucesso!')
    else:
        print('Falha ao deletar novo registro. Detalhes:', response)


list_tables()
print()
list_table_values()
print()
list_table_value_by_value('joao')
print()
create_item_in_table()
print()
delete_item_in_table('gisele2', 'gcj')