from database import Database

class FootballDB:
    def __init__(self, database:Database):
        self.db = database
        self.num_match = 1

    def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, teams, score):
        query = "CREATE (:Match {name: $name, teams: $teams, score: $score})"
        parameters = {"name": "Match " + str(self.num_match), "teams": teams, "score": score}
        self.db.execute_query(query, parameters)
        self.num_match += 1

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_matches(self):
        query = "MATCH (m:Match) RETURN m.name AS name, m.teams AS teams, m.score AS score"
        results = self.db.execute_query(query)
        return [(result["nome"], result["teams"], result["score"]) for result in results]
    
    def get_match(self, match_name):
        query = "MATCH (m:Match{name:$match_name}) RETURN m.name AS name, m.teams AS teams, m.score AS score"
        parameters = {"match_name":match_name}
        results = self.db.execute_query(query, parameters)
        return [(result["name"], result["teams"], result["score"]) for result in results]
    
    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player{name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    def insert_player_match(self, player_name, match_name, player_rating):
        query = "MATCH (p:Player {name: $player_name}),(m:Match {name: $match_name}) CREATE (p)-[:PLAYED{rating:$player_rating}]->(m)"
        parameters = {"player_name": player_name, "match_name": match_name, "player_rating": player_rating}
        self.db.execute_query(query, parameters)

    def get_players_from_match(self, match_name):
        query = "MATCH (p:Player)-[pp:PLAYED]->(m:Match{name:$match_name}) RETURN p.name AS name"
        parameters = {"match_name": match_name}
        results = self.db.execute_query(query, parameters)
        return [(result['name']) for result in results]

    def get_matches_from_player(self, player_name):
        query = "MATCH (p:Player{name:$player_name})-[pp:PLAYED]->(m:Match) RETURN m.name AS name, m.teams AS teams, m.score AS score, pp.rating AS rating"
        parameters = {"player_name": player_name}
        results = self.db.execute_query(query, parameters)
        return [(result['name'], result['teams'], result['score'], result['rating']) for result in results]
