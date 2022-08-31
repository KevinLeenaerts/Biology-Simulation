class Settings:
    grid_size = 50;
    iterations = 100;
    starting_entity_amount = 3;
    mutationChance = 0.3;
    allowed_mutation_iteration = round(0.3 * iterations);
    
    food_spawns = round((1/9) * (grid_size ** 2));
    standard_energy = grid_size;
    standard_speed = 1;
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    textOffset = 0.9;
    checkingIterations = 5

