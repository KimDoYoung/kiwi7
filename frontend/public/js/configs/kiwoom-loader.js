// static/js/configs/kiwoom-loader.js
window.loadKiwoomConfig = async function(configKey) {
    if (window.KiwoomConfigs?.[configKey]) {
        return Promise.resolve(window.KiwoomConfigs[configKey]);
    }

    const path = `/public/js/configs/kiwoom/${configKey}.js`;
    return new Promise((resolve, reject) => {
        const script = document.createElement("script");
        script.src = path;
        script.onload = () => {
            if (window.KiwoomConfigs?.[configKey]) {
                resolve(window.KiwoomConfigs[configKey]);
            } else {
                reject(new Error(`Config for ${configKey} not found in loaded script.`));
            }
        };
        script.onerror = () => reject(new Error(`Failed to load script: ${path}`));
        document.head.appendChild(script);
    });
};
