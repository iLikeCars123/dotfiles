" ===== plugins list =====
call plug#begin('~/.vim/plugged')

Plug 'itchyny/lightline.vim'
Plug 'preservim/nerdtree'
Plug 'tpope/vim-commentary'
Plug 'ryanoasis/vim-devicons'
Plug 'joshdick/onedark.vim'
call plug#end()

" ===== vim builtin config =====
" set termguicolors
set encoding=UTF-8
set showtabline=2
set laststatus=2
set number
set noshowmode
set relativenumber
set rnu
set t_Co=16
set tabstop=4
set shiftwidth=4
set expandtab
set showmatch
set ignorecase
set hlsearch
set incsearch
set softtabstop=4
set autoindent
filetype plugin indent on
set clipboard=unnamedplus

let g:snipMate = { 'snippet_version' : 1 }
cnoreabbrev vst vsplit term://zsh<bar>vertical resize 40
" Use ctrl-[hjkl] to select the active split!
nmap <silent> <c-k> :wincmd k<CR>
nmap <silent> <c-j> :wincmd j<CR>
nmap <silent> <c-h> :wincmd h<CR>
nmap <silent> <c-l> :wincmd l<CR>
inoremap <A-j> <Esc>:m .+1<CR>==gi
inoremap <A-k> <Esc>:m .-2<CR>==gi
vnoremap <A-j> :m '>+1<CR>gv=gv
vnoremap <A-k> :m '<-2<CR>gv=gv
nnoremap <C-Left> :tabprevious<CR>
nnoremap <C-Right> :tabnext<CR>
inoremap jj <Esc>
nmap <silent> <F2> :NERDTreeToggle<CR> 
nmap <silent> <F3> :vst<CR> 
tnoremap <Esc> <C-\><C-n>
tnoremap jj <C-\><C-n>

" Theme
"Use 24-bit (true-color) mode in Vim/Neovim when outside tmux.
"If you're using tmux version 2.2 or later, you can remove the outermost $TMUX check and use tmux's 24-bit color support
"(see < http://sunaku.github.io/tmux-24bit-color.html#usage > for more information.)
if (empty($TMUX))
  if (has("nvim"))
    "For Neovim 0.1.3 and 0.1.4 < https://github.com/neovim/neovim/pull/2198 >
    let $NVIM_TUI_ENABLE_TRUE_COLOR=1
  endif
  "For Neovim > 0.1.5 and Vim > patch 7.4.1799 < https://github.com/vim/vim/commit/61be73bb0f965a895bfb064ea3e55476ac175162 >
  "Based on Vim patch 7.4.1770 (`guicolors` option) < https://github.com/vim/vim/commit/8a633e3427b47286869aa4b96f2bfc1fe65b25cd >
  " < https://github.com/neovim/neovim/wiki/Following-HEAD#20160511 >
  if (has("termguicolors"))
    set termguicolors
  endif
endif
let g:lightline = {
       \ 'colorscheme': 'onedark',
       \ }
syntax enable
colorscheme onedark
hi Normal guibg=NONE ctermbg=NONE
hi LineNr guibg=NONE ctermbg=NONE
hi SignColumn guibg=NONE ctermbg=NONE
hi EndOfBuffer guibg=NONE ctermbg=NONE
