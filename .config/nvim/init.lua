require('config.lazy')

local opt = vim.opt
local map = vim.keymap.set
local tscope = require('telescope.builtin')

opt.cursorline = true               -- Подсветка строки с курсором
opt.number = true                   -- Включаем нумерацию строк
opt.relativenumber = true           -- Включаем относительные номера
opt.splitright = true               -- vertical split вправо
opt.splitbelow = true               -- horizontal split вниз
opt.shiftwidth = 2                  -- shift 2 spaces when tab
opt.tabstop = 2                     -- 1 tab == 2 spaces
opt.smartindent = true              -- autoindent new lines
opt.clipboard = 'unnamedplus'       -- системный буфер обмена

opt.foldmethod = 'indent'
opt.foldlevel = 999


vim.keymap.leader = ' '
map('n', '<leader>s', '<cmd>w<CR>')
map('n', '<leader>w', '<cmd>qa!<CR>')
map('n', '<leader>e', tscope.find_files)
map('n', '<leader>t', '<cmd>Neotree float<CR>')
map('n', '`', '@')
map({'n', 'v'}, 'w', 'b')
map({'n', 'v'}, 'e', 'w')
