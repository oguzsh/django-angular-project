import {Component} from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Home';

  constructor(private _http: HttpClient) {
    this.note.noteTitle = 'Example Note';
    this.user.name = 'Example User';
  }

  user: User = new User();
  note: Note = new Note();

  handleNote() {
    this.getNotes().subscribe(n => this.note.noteTitle = n.results[0].noteTitle);
  }

  handleUser() {
    this.getUsers().subscribe(u => this.user.name = u.results[0].name);
  }


  getNotes() {
    return this._http.get<Note>('http://localhost:8000/api/notes/');
  }

  getUsers() {
    return this._http.get<User>('http://localhost:8000/api/users/');
  }

}

export class User {
  name: string;
  surname: string;
  notes: string;
  results: any;
}

export class Note {
  noteTitle: string;
  results: any;
}
