from gql import gql

try:
    from ..db.init import client
except Exception as e:
    from plugins.db.init import client


# Пример вызова DataSpace с подписью
def insert_value_to_audit(user_id: str,
                          session_id: str,
                          text: str):
    query = gql("""mutation ($text: String!, $sessionId: String!, $userId: String!){
  p1: packet {
    createLogData(input: {
      text: $text,
      sessionId: $sessionId,
      userId: $userId
    }){
      text
    }
  }
}""")
    variable_values = {
        "text": text,
        "sessionId": session_id,
        "userId": user_id
    }
    return client.execute(query, variable_values=variable_values)


def insert_value_to_model(bin_text: str,
                          model_revision: str):
    query = gql("""mutation ($binText: String!, $modelRevision: String!){
  p1: packet {
    createModelData(input: {
      binText: $binText,
      modelRevision: $modelRevision
    }){
      modelRevision
    }
  }
}""")
    variable_values = {
        "binText": bin_text,
        "modelRevision": model_revision,
    }
    return client.execute(query, variable_values=variable_values)


def get_base64_model_from_base(limit: int, offset: int, model_revision: str):
    query = gql("""query FetchModel($limit: Int!, $offset: Int!, $cond: String!){
  searchModelData(limit: $limit, offset: $offset, cond: $cond) {
    elems {
      binText
      modelRevision
    }
  }
}""")

    variable_values = {
        "limit": limit,
        "offset": offset,
        "cond": model_revision
    }
    return client.execute(query, variable_values=variable_values)
