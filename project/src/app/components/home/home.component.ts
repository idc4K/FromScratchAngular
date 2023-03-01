import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Movie } from 'src/app/model';
import { ServiceService } from 'src/app/services/service.service';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})



export class HomeComponent implements OnInit{
  public sort ! : string;
  public movie  ! : Movie[]

  constructor(private service : ServiceService, private route:ActivatedRoute){}
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
    this.service
      .getAllData(sort, search)
      .subscribe((data) => {
        this.movie = data
        console.log(data)
      })
  }
}
