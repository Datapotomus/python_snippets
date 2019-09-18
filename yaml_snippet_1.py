import yaml
key_lookup='companies'

with open('data.yaml') as file:
    
    yaml_data = yaml.load_all(file, Loader=yaml.FullLoader)

    for data in yaml_data:
        
        for key, v in data.items():
            # print(key, "->", v)

            if key == key_lookup:
                print(key, "-->", v[0])
