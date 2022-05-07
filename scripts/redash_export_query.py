from redash_toolbelt.client import Redash

template = u"""/*
Name: {name}
Data source: {data_source}
Created By: {created_by}
Last Updated At: {last_updated_at}
*/
{query}"""





def save_queries(queries):
    for query in queries:
        filename = "query_{}.sql".format(query["id"])
        with open(filename, "w") as f:
            content = template.format(
                name=query["name"],
                data_source=query["data_source_id"],
                created_by=query["user"]["name"],
                last_updated_at=query["updated_at"],
                query=query["query"],
            )
            f.write(content)

def export_queries():
    redash_api = 'F23HKin8rRi9nNmuf7m20X2QFqvmv93atp8BKZ9c'
    redash_url = 'http://localhost:5000'

    redash = Redash(redash_url, redash_api)
    queries = redash.paginate(redash.queries)
    save_queries(queries)

export_queries()