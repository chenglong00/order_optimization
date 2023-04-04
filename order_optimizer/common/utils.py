from order_optimizer.api.model import Contact


def dict_to_contract(dict_list):
    contract_list = []
    for dict in dict_list:
        contract_list.append(Contact(name=dict.get("name"),
                                     start=dict.get("start"),
                                     duration=dict.get("duration"),
                                     price=dict.get("price")
                                     ))

    return contract_list
