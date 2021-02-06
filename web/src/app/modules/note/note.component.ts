import { Component, OnInit } from '@angular/core';

import { BsModalService } from 'ngx-bootstrap/modal';
import { EventEmitterService } from 'src/app/core/services/event-emitter/event-emitter.service';

@Component({
  selector: 'app-note',
  templateUrl: './note.component.html',
  styleUrls: ['./note.component.scss'],
})
export class NoteComponent implements OnInit {
  constructor(
    private modalService: BsModalService,
    private eventEmitterService: EventEmitterService
  ) {
  }

  ngOnInit() {
    console.log('dasdasdad');
    this.eventEmitterService.noteSubscription = this.eventEmitterService.invokeNote.subscribe(
      (event: any) => {
        this.openModal(event);
      }
    );
  }

  openModal(event: any) {
    console.log(event);
    this.modalService.show('duasihdasuhgdiasdyusa');
  }
}
