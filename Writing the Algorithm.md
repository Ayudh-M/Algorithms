FUNCTION Backtrack(current_solution):
    IF isSolution(current_solution) THEN
        processSolution(current_solution)
        RETURN
    END IF

    FOR each option in optionsList DO
        IF isValid(option, current_solution) THEN
            add option to current_solution
            Backtrack(current_solution)
            remove option from current_solution (this is the actual backtracking step)
        END IF
    END FOR
END FUNCTION


### Define the Helper Functions:

- **isSolution()**: This function checks if the current solution is complete. For example, 
1. in a maze, it checks if we've reached the exit. 
2. like there are going to be multiple runs to solve the maze or
3. place a queen in a row or 
4. visit all cities in a country for the mail problem.
    
- **processSolution()**: This function processes the solution once it's found. For example, 
- it might print the solution or store it in a list. (this is what we have been doing for most of the things)
    
- **isValid()**: This function checks if the current option can be added to the current solution. This is where the pruning happens. If you can determine that adding the current option will not lead to a valid solution, you can prune that option.