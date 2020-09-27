import Recipes from './Recipes.svelte'
import User from './User.svelte'
import Recipe from './Recipe.svelte'
import RecipeAdd from './RecipeAdd.svelte'
import NotFound from './NotFound.svelte'

export const routes = {
    // Exact path
    '/': Recipes,

    // Using named parameters, with last being optional
    '/user/:id': User,

    '/recipe/add' :RecipeAdd,

    // Wildcard parameter
    '/recipe/:id': Recipe,


    // Catch-all
    // This is optional, but if present it must be the last
    '*': NotFound,
}