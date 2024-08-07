import type { StoryObj } from "@storybook/web-components";

import { html } from "lit";

import "@patternfly/patternfly/components/Login/login.css";

import { AuthenticatorTOTPChallenge, UiThemeEnum } from "@goauthentik/api";

import "../../../stories/flow-interface";
import "./AuthenticatorTOTPStage";

export default {
    title: "Flow / Stages / AuthenticatorTOTPStage",
};

export const LoadingNoChallenge = () => {
    return html`<ak-storybook-interface theme=${UiThemeEnum.Dark}>
        <div class="pf-c-login">
            <div class="pf-c-login__container">
                <div class="pf-c-login__main">
                    <ak-stage-authenticator-totp></ak-stage-authenticator-totp>
                </div>
            </div>
        </div>
    </ak-storybook-interface>`;
};

export const Challenge: StoryObj = {
    render: ({ theme, challenge }) => {
        return html`<ak-storybook-interface theme=${theme}>
            <div class="pf-c-login">
                <div class="pf-c-login__container">
                    <div class="pf-c-login__main">
                        <ak-stage-authenticator-totp
                            .challenge=${challenge}
                        ></ak-stage-authenticator-totp>
                    </div>
                </div></div
        ></ak-storybook-interface>`;
    },
    args: {
        theme: "automatic",
        challenge: {
            pendingUser: "foo",
            pendingUserAvatar: "https://picsum.photos/64",
            configUrl: "",
        } as AuthenticatorTOTPChallenge,
    },
    argTypes: {
        theme: {
            options: [UiThemeEnum.Automatic, UiThemeEnum.Light, UiThemeEnum.Dark],
            control: {
                type: "select",
            },
        },
    },
};
