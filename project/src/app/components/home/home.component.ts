import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Movie } from 'src/app/model';
import { ServiceService } from 'src/app/services/service.service';
import { APIResponse } from 'src/app/model';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit{
  public sort ! : string
  public movie ! : Array<Movie>

  constructor(private servicie : ServiceService, private route:ActivatedRoute){}
  ngOnInit(): void {

     
      this.route.params.subscribe((params:Params) => {
        if(params['movie-search']){
          this.searchMovie('name', params['movie-search'])
        }
        else{
          this.searchMovie('name')
        }
        return 
      })

      
  }
  searchMovie(sort:string,search ?:string):void{
    this.servicie
      .getAllData(sort, search)
      .subscribe((movieList: APIResponse<Movie>) => {
        this.movie = movieList.results
        console.log(movieList)
      })
  }
}
