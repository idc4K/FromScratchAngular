import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Movie } from 'src/app/model';
import { ServiceService } from 'src/app/services/service.service';
import { APIresponse } from 'src/app/model';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})



export class HomeComponent implements OnInit{
  public sort ! : string;
  public movies  : any
  public tri ! : Array<Movie>

  constructor(private service : ServiceService, private route:ActivatedRoute){}
  ngOnInit(): void {
     
      this.route.params.subscribe((params:Params) => {
        
        if(params['movie-search']){
          this.searchMovie('name', params['movie-search'])
        }
        else{
          this.searchMovie('name')
        }
        
      });

      this.getAll()
  }

  getAll(){
    this.service.listMovie().subscribe(data =>{
      this.movies = data
      console.log(data)
    })
  }
  searchMovie(sort:string,search ?:string):void{
     this.service
      .getAllData(sort, search)
      .subscribe(data => {
        this.tri = data.results
         
      })
  }
}
