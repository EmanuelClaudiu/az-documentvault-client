import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-root',
  imports: [],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  protected readonly title = signal('documentvault-client');
  inputFile: File | null = null;

  onFileUploaded(files: FileList | null) {
    if (files == null || files.length == 0) return;

    this.inputFile = files.item(0);
    debugger;
  }
}
