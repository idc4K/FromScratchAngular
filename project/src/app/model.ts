export interface Movie {
    name : string;
    desc : string;
    image : string;
    genre_movie : Array<Genre>
};


interface Genre{
    name : string
}

export interface APIresponse<T>{
    results : Array<T>
}
// export interface test{
//     name : string
//   }