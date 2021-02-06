import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { NavBarComponent } from './modules/nav-bar/nav-bar.component';
import { FooterComponent } from './modules/footer/footer.component';
import { GraphComponent } from './modules/graph/graph.component';

import { BsDropdownModule } from 'ngx-bootstrap/dropdown';
import { TooltipModule } from 'ngx-bootstrap/tooltip';
import { ModalModule } from 'ngx-bootstrap/modal';
import { NgxGraphModule } from '@swimlane/ngx-graph';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { NoteComponent } from './modules/note/note.component';
import { EventEmitterService } from './core/services/event-emitter/event-emitter.service';
import { AppRoutingModule } from './app-routing.module';

@NgModule({
  declarations: [
    AppComponent,
    NavBarComponent,
    FooterComponent,
    GraphComponent,
    NoteComponent
  ],
  imports: [
    BrowserModule,
    BsDropdownModule,
    TooltipModule,
    ModalModule,
    NgxGraphModule,
    BrowserAnimationsModule,
    NgxChartsModule,
    AppRoutingModule,
  ],
  providers: [
    EventEmitterService
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
