import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Movie } from '../model';

import { environment as env } from 'src/environments/environments';

@Injectable({
  providedIn: 'root'
})
export class ServiceService {

  constructor(private http : HttpClient) { }

  getAllData(ordering : string, search?:string) : Observable<Movie[]> {
    let params = new HttpParams().set('ordering',ordering)

    if(search){
      params = new HttpParams().set('ordering',ordering).set('search', search)
    }
    return this.http.get<Movie[]>(`${env.BASE_URL}/viewAllMovie`,{
      params : params
    });
  }
}
