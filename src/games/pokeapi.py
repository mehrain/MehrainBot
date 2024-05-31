import pokebase as pb

class PokemonStat:     
    def __init__(self, name, base_stat, effort):
        self.name = name
        self.base_stat = base_stat
        self.effort = effort
        self.url = f'https://pokeapi.co/api/v2/stat/{name}/'

    def __str__(self):
        return f'{self.name} - {self.base_stat} - {self.effort}'
    
    def __repr__(self):
        return f'{self.name} - {self.base_stat} - {self.effort}'


class PokeApi:
        
    def get_pokemon(self, poke_name, is_shiny, is_female):
        pokemon = pb.pokemon(poke_name)
        sprite = pb.SpriteResource('pokemon', pokemon.id, female=is_female, back=False, other=False, shiny=is_shiny)
        
        stats = []
        
        for stat in pokemon.stats:
            stats.append(PokemonStat(stat.stat.name, stat.base_stat, stat.effort))

        # Create object to return.
        return PokeResponse(pokemon.name, sprite.url, stats) 

class PokeResponse:
    
    def __init__(self, name, sprite, stats):
        self.name = name
        self.sprite = sprite
        self.stats = stats