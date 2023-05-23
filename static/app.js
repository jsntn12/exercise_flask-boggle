class BoggleGame {
	constructor(boardID) {
		this.board = $(`#${boardID}`);
		this.words = new Set();
	}
	async handleSubmit(evt) {
		evt.preventDefault();
		const $word = $('.word', this.board);
		let word = $word.val();

		if (this.words.has(word)) {
			return;
		}
	}
}
