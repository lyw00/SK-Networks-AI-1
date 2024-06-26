import actions, { AuthenticationActions } from "./actions"
import state, { AuthenticationState } from "./states"

export interface AuthenticationModule {
    namespaced: true
    state: Authenticationtate
    actions: AuthenticationActions
    mutations: AuthenticationMutations
}

const authenticationModule: AuthenticationModule = {
    namespaced: true,
    state,
    actions,
    mutations,
}

export default authenticationModule