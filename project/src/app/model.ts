export interface Movie{
    name : string,
    desc : string,
    image : string,
    genre_movie : string
}

export interface APIResponse<T>{
    results : Array<T>
}