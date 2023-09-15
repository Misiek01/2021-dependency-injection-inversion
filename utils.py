from random import sample

def api_get_data_from_db():
    random_sample = sample(range(100),k=3)
    return {"ids": random_sample}


class OrderInterface:

    def get_ids(self):
        data = api_get_data_from_db()
        return data.get("ids")
