odoo.define('odoo_outlook.Thread', function (require) {
"use strict";

var core = require('web.core');
var Widget = require('web.Widget');
var Thread = require('mail.ChatThread');
var Model = require('web.Model');
var mailMsgModel = new Model('mail.message');

var QWeb = core.qweb;
var _t = core._t;

var ORDER = {
    ASC: 1,
    DESC: -1,
};

Thread.include({
    render: function (messages, options) {
        clearTimeout(this.auto_render_timeout);
        var self = this;
        var msgs = _.map(messages, this._preprocess_message.bind(this));
        if (this.options.display_order === ORDER.DESC) {
            msgs.reverse();
        }
        options = _.extend({}, this.options, options);

        // Hide avatar and info of a message if that message and the previous
        // one are both comments wrote by the same author at the same minute
        // and in the same document (users can now post message in documents
        // directly from a channel that follows it)
        var prev_msg;
        var from_outlook_queries = []
        _.each(msgs, function (msg) {
            if (!prev_msg || (Math.abs(msg.date.diff(prev_msg.date)) > 60000) ||
                prev_msg.message_type !== 'comment' || msg.message_type !== 'comment' ||
                (prev_msg.author_id[0] !== msg.author_id[0]) || prev_msg.model !== msg.model ||
                prev_msg.res_id !== msg.res_id) {
                msg.display_author = true;
            } else {
                msg.display_author = !options.squash_close_messages;
            }
            from_outlook_queries.push(
                mailMsgModel.call('search_read', [[['id', '=', msg.id]]], {'fields': ['id', 'from_outlook']})
                    .then(function (data) {
                        if (data){ msg['from_outlook'] = data[0].from_outlook }
                    })
            )
            prev_msg = msg;
        });

        $.when.apply($, from_outlook_queries).done(function() {
            self.$el.html(QWeb.render('mail.ChatThread', {
                messages: msgs,
                options: options,
                ORDER: ORDER,
            }));
            self.auto_render_timeout = setTimeout(function () {
                if (!self.isDestroyed()) {
                    self.render(messages, options);
                }
            }, 1000*60); // re-render the thread every minute to update dates
        })


    },
})
})