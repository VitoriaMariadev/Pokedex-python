import conect as ct

conexao = ct.Connection()

pokemons = conexao.query(f"""
SELECT pokemon_info_id, nome, descricao, altura, peso, categoria_id, genero_id, total, hp, ataque, defesa, especial_ataque, especial_defesa, velocidade
	FROM pokemon_info;""")

for id, nome, descricao, altura, peso, categoria_id, genero_id, total, hp, ataque, defesa, especial_ataque, especial_defesa, velocidade in pokemons:
    print(f"""
          Nome: {nome}
          Descrição: {descricao}
          Altura: {altura}
          Peso: {peso}
          Categoria_id: {categoria_id}
          Genero_id: {genero_id}
          Total: {total}
          Hp: {hp}
          Ataque: {ataque}
          Defesa: {defesa}
          Especial_ataque: {especial_ataque}
          Especial_defesa: {especial_defesa}
          Velocidade: {velocidade}
            
          """)