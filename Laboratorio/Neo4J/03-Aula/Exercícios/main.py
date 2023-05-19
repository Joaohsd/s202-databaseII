from database import Database
from football import FootballDB

# Cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.231.26.228:7687", "neo4j", "altitude-tuition-cubes")
db.drop_all()

# Criando uma instância da classe FootballDB para interagir com o banco de dados
football_db = FootballDB(db)

# Cria os jogadores
football_db.create_player("João")
football_db.create_player("Pedro")
football_db.create_player("Miguel")
football_db.create_player("José")

# Cria as partidas
football_db.create_match(["Barcelona","Real Madrid"], [2,1])
football_db.create_match(["Inter de Milão","Real Madrid"], [1,1])
football_db.create_match(["Arsenal","Machester City"], [1,4])
football_db.create_match(["Bayern de Munique","Borussia Dortmund"], [2,0])

# Criando as relações

# Match 1
football_db.insert_player_match("João", "Match 1", 6.5)
football_db.insert_player_match("Miguel", "Match 1", 7.5)
football_db.insert_player_match("Pedro", "Match 1", 7.0)
football_db.insert_player_match("José", "Match 1", 8.0)

# Match 2
football_db.insert_player_match("João", "Match 2", 6.0)
football_db.insert_player_match("Miguel", "Match 2", 7.0)
football_db.insert_player_match("Pedro", "Match 2", 8.0)

# Match 3
football_db.insert_player_match("José", "Match 3", 8.0)
football_db.insert_player_match("Miguel", "Match 3", 7.5)
football_db.insert_player_match("Pedro", "Match 3", 6.5)

# Match 4
football_db.insert_player_match("José", "Match 4", 8.0)
football_db.insert_player_match("Miguel", "Match 4", 7.5)
football_db.insert_player_match("Pedro", "Match 4", 6.5)
football_db.insert_player_match("João", "Match 4", 6.5)

# Partidas jogadas pelo João
print(football_db.get_matches_from_player("João"))
# Partidas jogadas pelo José
print(football_db.get_matches_from_player("José"))
# Jogadores que jogaram a Match 1
print(football_db.get_players_from_match("Match 1"))
# Jogadores que jogaram a Match 3
print(football_db.get_players_from_match("Match 3"))

# Atualiza o Miguel
football_db.update_player("Miguel","Messi")

# Informação dos jogadores cadastrados
print(football_db.get_players())

# Exclui o José
football_db.delete_player("José")

# Informação dos jogadores cadastrados
print(football_db.get_players())

# Informações sobre a Match 1
print(football_db.get_match("Match 1"))

# Fechando a conexão
db.close()